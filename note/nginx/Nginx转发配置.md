# Nginx转发配置

### 显性URL转发

```yaml
server {
  listen 80;
  server_name weibo.utren.ml;
  rewrite ^(.*) http://weibo.com/u/6577948360;
}
```

