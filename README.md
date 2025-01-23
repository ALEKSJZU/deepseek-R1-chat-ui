# deepseek-R1-chat-ui
deepseek-R1的聊天ui
#windows平台安装依赖：
## 安装所有依赖
pip install -r requirements.txt

# 如果使用虚拟环境，先激活环境再安装：
venv\Scripts\activate  激活虚拟环境
pip install -r requirements.txt

#macos平台：
## 安装所有依赖
pip install -r requirements.txt

## 如果使用虚拟环境，先激活环境再安装：
source venv/bin/activate  激活虚拟环境
pip install -r requirements.txt

#请自行将API KEY加入环境变量，方法：

##Windows 设置环境变量：

###临时设置（命令行）：

## CMD
set API_KEY=your_api_key_here

## PowerShell
$env:API_KEY="your_api_key_here"

###永久设置（命令行）：

## CMD
setx API_KEY "your_api_key_here"

## PowerShell
[Environment]::SetEnvironmentVariable("API_KEY", "your_api_key_here", "User")
macOS 设置环境变量：

###临时设置（终端）：

export API_KEY=your_api_key_here

##永久设置：
编辑 shell 配置文件（根据你使用的 shell 选择）：

###对于 bash：
echo 'export API_KEY=your_api_key_here' >> ~/.bash_profile
source ~/.bash_profile
###对于 zsh：
echo 'export API_KEY=your_api_key_here' >> ~/.zshrc
source ~/.zshrc
###验证环境变量是否设置成功：
# Windows (CMD)
echo %API_KEY%

# Windows (PowerShell)
echo $env:API_KEY

# macOS
echo $API_KEY
当前版本未显示思考过程，如果需要请自行修改代码添加功能
