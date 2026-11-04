# 网易严选 App 自动化（Appium + PO + pytest）

原始过程式脚本保留在 `practice/启动.py`，根目录下是按 PO 分层封装后的代码。

## 目录

```text
test_app_heima/
├── base/
│   └── base_page.py       # 公共页面操作
├── page/
│   ├── launch_page.py     # 启动页
│   ├── main_page.py       # 首页
│   └── login_page.py      # 登录页
├── data/
│   ├── login_data.json
│   └── login_data.example.json
├── log/
├── report/
├── script/
│   ├── conftest.py        # driver、测试数据、失败截图
│   └── test_login.py      # 登录用例
├── practice/
│   └── 启动.py
├── config.py
├── tools.py
└── pytest.ini
```

## 分层关系

```text
script/test_login.py
        ↓ 调用页面动作
page/LoginPage.login_with_email()
        ↓ 调用公共操作
base/BasePage.click() / input_text() / is_displayed()
        ↓ 使用
tools.py + config.py
```

## BasePage 保留的方法

| 方法 | 作用 |
| --- | --- |
| `find` | 等待元素出现并返回 |
| `find_all` | 等待并返回所有匹配元素 |
| `find_clickable` | 等待元素可点击 |
| `click` | 点击元素 |
| `click_if_exists` | 可选弹窗：存在就点，不存在跳过 |
| `input_text` | 清空并输入 |
| `get_text` | 获取文本 |
| `is_displayed` | 判断元素是否可见 |
| `swipe` / `swipe_up` / `swipe_down` | 滑动 |
| `back` | 返回键 |
| `hide_keyboard` | 收起键盘 |
| `take_screenshot` | 保存截图 |

Page 层保留完整的页面动作，例如 `LoginPage` 中的
`accept_agreement()`、`choose_email_login()`、`login_with_email()`、
`is_login_success()`。

## 运行

```powershell
cd E:\AAAstudy\test_app_heima

# 启动 Appium
appium

# 确保 MuMu 已连接
adb connect 127.0.0.1:7555
adb devices

# 执行
pytest
```

只跑登录：

```powershell
pytest script/test_login.py -v
```

生成 HTML 报告（需要 `pytest-html`）：

```powershell
pip install -r requirements.txt
pytest --html=report/report.html --self-contained-html
```

## 登录数据

账号密码放在 `data/login_data.json`：

```json
{
  "account": "你的邮箱",
  "password": "你的密码"
}
```

该文件已加入 `.gitignore`，不要提交到仓库。

## 定位器

- 优先使用 `resource-id`，例如 `account_edit`、`password_edit`。
- “其他登录”和“邮箱登录”图标没有稳定文案，暂时使用
  `img_icon` 的第 2、4 个 `ImageView`，集中写在
  `practice/llogin_page.py` 顶部，App 改版时只改这里。
- 原脚本中“跳过”使用 `CLASS_NAME` 会点到同类 TextView，已改成
  `//*[@text='跳过']`。

## 等待说明

`BasePage` 中使用的是：

```python
WebDriverWait(driver, config.WAIT_TIME)
```

这里的 `WAIT_TIME` 是显式等待时间，默认 10 秒。不要写成
`config.IMPLICIT_WAIT`，否则等待时间可能为 0，元素还没加载就报错。
