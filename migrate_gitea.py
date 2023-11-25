# 将 ruleset 里面的 url 从 github链接 改为 gitea链接

github_old = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR"
gitea_new = "http://gitea.local:30008/root/ACL4SSR/raw/branch"

src_file = "Clash/config/ACL4SSR_Online_Full.ini"
target_file = "Clash/config/ACL4SSR_Online_Full_update.ini"

with open(src_file, "r", encoding="utf-8") as src, open(
    target_file, "w+", encoding="utf-8"
) as target:
    content = src.read()
    content = content.replace(github_old, gitea_new)
    target.write(content)
