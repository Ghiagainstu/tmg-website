# Git 设置指南

## 第一步：初始化Git仓库

打开PowerShell，执行以下命令：

```powershell
# 进入项目目录
cd "c:\Users\fireh\WorkBuddy\20260326144402\cmg-website"

# 初始化Git仓库
git init

# 创建.gitignore文件（可选，但推荐）
echo "*.log" > .gitignore
echo ".DS_Store" >> .gitignore
```

## 第二步：提交代码到Git

```powershell
# 添加所有文件
git add .

# 查看状态（确认要提交的文件）
git status

# 第一次提交
git commit -m "Initial commit: CMG website"

# 设置主分支
git branch -M main
```

## 第三步：在GitHub上创建仓库

1. 访问 https://github.com 并登录
2. 点击右上角 `+` 号 → `New repository`
3. 填写仓库名称：`cmg-website`
4. 选择 `Private`（私有）或 `Public`（公开）
5. **不要**勾选 "Initialize this repository with a README"
6. 点击 `Create repository`

## 第四步：连接到GitHub

在GitHub创建仓库后，复制仓库地址，然后在PowerShell中执行：

```powershell
# 添加远程仓库（替换你的GitHub用户名）
git remote add origin https://github.com/你的用户名/cmg-website.git

# 推送到GitHub
git push -u origin main
```

如果提示输入GitHub用户名和密码：
- 用户名：输入你的GitHub用户名
- 密码：需要使用 **Personal Access Token**，而不是登录密码

### 创建GitHub Personal Access Token

1. 访问 https://github.com/settings/tokens
2. 点击 `Generate new token` → `Generate new token (classic)`
3. 填写描述（比如 "CMG Website"）
4. 勾选 `repo` 权限
5. 点击 `Generate token`
6. 复制生成的token（只显示一次，要立即复制）

然后用这个token作为密码。

## 第五步：以后更新代码

```powershell
cd "c:\Users\fireh\WorkBuddy\20260326144402\cmg-website"

# 修改文件后...

# 查看修改了什么
git status

# 添加修改的文件
git add .

# 提交
git commit -m "描述你的修改内容"

# 推送到GitHub
git push
```

## 常用Git命令速查

| 命令 | 说明 |
|------|------|
| `git status` | 查看当前状态 |
| `git add .` | 添加所有修改 |
| `git commit -m "message"` | 提交修改 |
| `git push` | 推送到远程 |
| `git pull` | 从远程拉取最新代码 |
| `git log` | 查看提交历史 |
| `git diff` | 查看具体修改内容 |

## 下一步：部署到Vercel

完成以上步骤后，访问 https://vercel.com：
1. 登录Vercel账号
2. 点击 `Add New` → `Project`
3. 选择 `Import Git Repository`
4. 找到 `cmg-website` 仓库
5. 点击 `Import` → `Deploy`

以后每次推送代码到GitHub，Vercel会自动部署！
