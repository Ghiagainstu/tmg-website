# 网站开发经验教训

## 📌 核心经验（必须记住）

### 1. 官方图标库优先原则
**经验**: 永远优先使用官方图标库，而不是自己绘制

**为什么**:
- 自绘logo缺乏专业性，难以达到品牌标准
- 官方图标库（Simple Icons, Heroicons）提供经过验证的高质量图标
- 品牌logo有严格规范，随意修改会导致识别度下降

**行动清单**:
```
优先级顺序：
1. Simple Icons (3400+品牌官方图标)
2. 品牌官方网站的资源中心
3. Heroicons/Phosphor Icons（通用图标）
4. 自己绘制（仅作为最后选择）
```

### 2. CSS滤镜的正确使用
**经验**: 避免使用滤镜来改变颜色，使用`currentColor`

**错误做法**:
```css
❌ filter: brightness(0) invert(1);
```
**问题**: 副作用大，会把所有图片变成白色

**正确做法**:
```css
✅ fill: currentColor;
✅ color: var(--text-primary);
```

**教训**: 滤镜适合用于特效（模糊、透明度），不适合改变颜色

### 3. 设计系统是投资，不是成本
**经验**: 建立设计系统会节省大量时间

**投资回报**:
- 建立: 30分钟
- 后续每次节省: 10分钟
- 3次使用后开始净赚

**必须包含的要素**:
```css
:root {
  /* 颜色 */
  --color-primary: #3b82f6;
  --color-success: #10b981;
  --color-error: #ef4444;

  /* 字体 */
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;

  /* 间距 */
  --space-4: 1rem;
  --space-8: 2rem;
}
```

### 4. 工具验证要提前
**经验**: 在项目开始前测试所有工具是否可用

**错误流程**:
```
开始工作 → 发现工具不可用 → 被迫切换工具 → 延期
```

**正确流程**:
```
1. 列出所需工具清单
2. 逐一测试每个工具
3. 记录不可用的工具
4. 准备备选方案
5. 开始工作
```

---

## 🔍 具体问题与解决方案

### 问题1: Logo显示为纯白色
**现象**: 所有图片logo显示成纯白色

**诊断过程**:
1. 检查图片文件 → 文件正常
2. 检查HTML标签 → 结构正确
3. 搜索CSS规则 → 找到`filter: brightness(0) invert(1)`

**解决方案**:
```css
/* 移除滤镜 */
.hero__platform-logo {
  /* filter: brightness(0) invert(1); ← 删除这行 */
  object-fit: contain;
}
```

**预防措施**:
- 审查CSS时注意filter属性
- 使用浏览器开发者工具实时调试
- 对颜色相关的CSS规则保持警惕

### 问题2: Logo风格不统一
**迭代历程**:

| 版本 | 方案 | 结果 | 教训 |
|------|------|------|------|
| V1 | 自己绘制SVG | 用户不满意 | 自绘缺乏专业性 |
| V2 | 使用asset图片 | 显示为纯白 | 滤镜副作用 |
| V3 | Simple Icons | ✅ 成功 | 官方资源优先 |

**关键领悟**:
- 用户对"看起来专业"很敏感
- 3次迭代才找到正确方案
- 应该从V3开始，节省2次迭代

---

## 💡 技术决策指南

### 何时使用单文件HTML
✅ 适合:
- 简单落地页（1-3页）
- 个人博客/文档
- 快速原型
- 无需复杂状态管理

❌ 不适合:
- 大型SPA（10+页面）
- 需要多人协作
- 复杂交互逻辑
- 需要SEO优化

### 何时建立设计系统
✅ 必须:
- 有3个以上相同类型的组件
- 需要保持多个页面一致性
- 团队协作开发
- 后续会迭代维护

❌ 可选:
- 一次性页面
- 快速验证想法
- 独立Demo

### 何时使用SVG图标
✅ 适合:
- 需要多尺寸显示
- 品牌logo
- 简单图标（< 50KB）
- 需要动态改变颜色

❌ 不适合:
- 复杂插画（> 100KB）
- 需要透明度叠加
- 大量图标（建议用字体图标）

---

## 📊 性能优化检查清单

### 页面加载速度
- [ ] 内联关键CSS
- [ ] 使用SVG矢量图标
- [ ] 压缩图片
- [ ] 延迟加载非关键资源
- [ ] 使用CDN（如有外部资源）

### 用户体验
- [ ] 响应式设计（4个断点）
- [ ] 触摸目标最小44px
- [ ] 加载状态反馈
- [ ] 错误状态处理
- [ ] 空状态设计

### 可访问性
- [ ] 对比度≥ 4.5:1
- [ ] 键盘导航完整
- [ ] ARIA标签正确
- [ ] 屏幕阅读器友好
- [ ] 焦点管理清晰

---

## 🎯 快速决策树

### Logo选择流程
```
需要logo？
  ├─ 是 → 品牌logo？
  │       ├─ 是 → Simple Icons → ✅
  │       └─ 否 → Heroicons → ✅
  └─ 否 → 不需要
```

### CSS架构选择
```
项目规模？
  ├─ 小型（< 3页）→ 单文件CSS
  ├─ 中型（3-10页）→ CSS Modules
  └─ 大型（> 10页）→ CSS-in-JS
```

### 图标格式选择
```
图标需求？
  ├─ 品牌logo → SVG
  ├─ UI图标 → SVG或字体图标
  └─ 插画 → SVG或WebP
```

---

## 🔧 常用命令和工具

### 图标资源
```bash
# Simple Icons CDN
https://cdn.simpleicons.org/{brand}

# GitHub原始文件
https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{brand}.svg

# 搜索图标
https://simpleicons.org/?q={brand}
```

### 性能测试
```bash
# Lighthouse
lighthouse https://your-site.com --view

# WebPageTest
https://www.webpagetest.org/

# PageSpeed Insights
https://pagespeed.web.dev/
```

### CSS验证
```bash
# CSS校验
https://jigsaw.w3.org/css-validator/

# HTML校验
https://validator.w3.org/
```

---

## 📚 推荐资源

### 设计系统
- [Design Systems](https://www.designsystems.com/)
- [Material Design](https://material.io/design)
- [Ant Design](https://ant.design/)

### 图标库
- [Simple Icons](https://simpleicons.org) - 品牌图标
- [Heroicons](https://heroicons.com) - 通用图标
- [Phosphor Icons](https://phosphoricons.com) - 现代风格

### 性能优化
- [Web.dev](https://web.dev/)
- [CSS-Tricks](https://css-tricks.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

## ✅ 快速检查表

### 开始项目前
- [ ] 测试所有工具可用性
- [ ] 确定技术栈
- [ ] 建立设计系统
- [ ] 准备备选方案

### 开发过程中
- [ ] 定期预览效果
- [ ] 检查代码一致性
- [ ] 测试响应式
- [ ] 验证可访问性

### 交付前
- [ ] 性能测试
- [ ] 跨浏览器测试
- [ ] 代码审查
- [ ] 文档整理

---

**文档版本**: v1.0
**更新时间**: 2026年3月28日
**适用场景**: 静态网站开发、前端设计系统
