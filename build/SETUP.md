# Farm Insight BE – Deployment Notes

This repo lives at `/home/farm-insight-be`. The commands below assume you run them inside that folder and the virtualenv is `/home/farm-insight-be/venv` (no leading dot).

## Prepare environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Database & static assets
```bash
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput    # output -> ./staticfiles
python manage.py seed_form_templates
```

## Run (development)
```bash
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

## Run (production via Gunicorn + Uvicorn worker)
```bash
source venv/bin/activate
gunicorn app:app -w 1 -k uvicorn.workers.UvicornWorker \
  --bind unix:$(pwd)/run/farm-insight.sock \
  --access-logfile logs/access.log \
  --error-logfile logs/error.log
```
Prereqs: create paths once: `mkdir -p run logs staticfiles`.

## systemd unit (example)
Save as `/etc/systemd/system/farm-insight.service` (adjust paths and secrets):
```
[Unit]
Description=Farm Insight Django API
After=network.target

[Service]
# Set to an existing user on the server (e.g. root or www-data)
User=root
Group=root
WorkingDirectory=/home/farm-insight-be
Environment="DJANGO_SETTINGS_MODULE=config.settings"
Environment="DJANGO_SECRET_KEY=change-me"
Environment="DJANGO_DEBUG=false"
ExecStart=/home/farm-insight-be/venv/bin/gunicorn config.asgi:application \
    -w 1 -k uvicorn.workers.UvicornWorker \
    --bind unix:/home/farm-insight-be/run/farm-insight.sock \
    --access-logfile /home/farm-insight-be/logs/access.log \
    --error-logfile /home/farm-insight-be/logs/error.log
Restart=always

[Install]
WantedBy=multi-user.target
```
Enable: `sudo systemctl daemon-reload && sudo systemctl enable --now farm-insight`.

## Nginx reverse proxy (example)
`/etc/nginx/sites-available/farm-insight.conf`:
```
server {
    listen 81;
    server_name isatsbangkhaosat.com;

    location /static/ {
        alias /home/farm-insight-be/staticfiles/;
    }

    location / {
        proxy_pass http://unix:/home/farm-insight-be/run/farm-insight.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Enable: `sudo ln -s /etc/nginx/sites-available/farm-insight.conf /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl restart nginx`.

## Serve frontend (static build) on port 80
Giả sử FE đã build tại `/home/farm-insight-be/dist` (file `index.html` nằm trong dist). Tạo vhost Nginx mới:

```
sudo tee /etc/nginx/sites-available/farm-insight-fe.conf > /dev/null <<'EOF'
server {
    listen 80;
    server_name isatsbangkhaosat.com;

    root /home/farm-insight-be/dist;
    index index.html;

    # Single Page App fallback
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Optional: serve static assets with caching
    location ~* \.(js|css|png|jpg|jpeg|gif|svg|ico|woff2?)$ {
        try_files $uri =404;
        access_log off;
        add_header Cache-Control "public, max-age=31536000";
    }
}
EOF

sudo ln -sf /etc/nginx/sites-available/farm-insight-fe.conf /etc/nginx/sites-enabled/farm-insight-fe.conf
sudo nginx -t && sudo systemctl reload nginx
```

Lưu ý:
- Đặt đúng đường dẫn `root` tới thư mục `dist` của FE (`/home/farm-insight-be/dist`).
- Port 80 sẽ phục vụ FE, API vẫn ở 81 qua vhost khác.


Reload và restart:
sudo systemctl daemon-reload
sudo systemctl restart farm-insight
