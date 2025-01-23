# deepseek-R1-chat-ui

deepseek-R1的聊天ui

## Windows 平台安装依赖

### 安装所有依赖
```bash
pip install -r requirements.txt
```

### 使用虚拟环境
```bash
venv\Scripts\activate  # 激活虚拟环境
pip install -r requirements.txt
```

## macOS 平台

### 安装所有依赖
```bash
pip install -r requirements.txt
```

### 使用虚拟环境
```bash
source venv/bin/activate  # 激活虚拟环境
pip install -r requirements.txt
```

## API KEY 环境变量设置

### Windows 设置环境变量

#### 临时设置（命令行）

CMD:
```cmd
set API_KEY=your_api_key_here
```

PowerShell:
```powershell
$env:API_KEY="your_api_key_here"
```

#### 永久设置（命令行）

CMD:
```cmd
setx API_KEY "your_api_key_here"
```

PowerShell:
```powershell
[Environment]::SetEnvironmentVariable("API_KEY", "your_api_key_here", "User")
```

### macOS 设置环境变量

#### 临时设置（终端）
```bash
export API_KEY=your_api_key_here
```

#### 永久设置
编辑 shell 配置文件（根据你使用的 shell 选择）：

对于 bash：
```bash
echo 'export API_KEY=your_api_key_here' >> ~/.bash_profile
source ~/.bash_profile
```

对于 zsh：
```bash
echo 'export API_KEY=your_api_key_here' >> ~/.zshrc
source ~/.zshrc
```

### 验证环境变量设置

Windows (CMD):
```cmd
echo %API_KEY%
```

Windows (PowerShell):
```powershell
echo $env:API_KEY
```

macOS:
```bash
echo $API_KEY
```
运行：
```bash
streamlit run ui.py
```
注：思考过程在聊天结果底部展开
