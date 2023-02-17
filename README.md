# APPIUM
APPIUM

APPIUM Repositories
https://github.com/orgs/appium/repositories


Instalar python
Instalar pycharm
Instalar appium library with pip install Appium-Python-Client
Instalar appium server gui 
Navigate to https://github.com/appium/appium-desktop and goto Releases section on GitHub, download the latest release
Instalar appium inspector
Instalar android studio and environment variables
Once android studio is installed click on configure or more options -> sdk manager -> select the options we want to install and click Ok.
Instalar el JDK y ejecutar el comando en la terminal echo $(/usr/libexec/java_home)
Copiar la ruta que devuelve y abrir appium server -> click edit configurations y pegar la ruta en el JAVA_HOME

AÑADIR ADB TO PATH ENVIRONMENT VARIABLES
Copiamos la ruta donde se encuentra el Android/sdk: este dato lo podemos obtener de android studio -> more actions -> sdk manager, aquí podemos encontrar el Android sdk location
Luego abrimos una terminal y ejecutamos el comando vim ~/.zshrc
Presionamos la tecla i para insertar datos y ponemos lo siguiente:
export ANDROID_HOME=/Users/rene.cortes/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
Una vez terminado presionamos ESC -> x para salir del documento y guardar los cambios
Ejecutamos source ~/.bash_profile
Cerramos la terminal y abrimos una nueva y ejecutamos adb devices, ya nos debería reconocer los comandos adb y aparecer el siguiente letrero:
rene.cortes@WIZELINE ~ % adb devices
* daemon not running; starting now at tcp:5037
* daemon started successfully
List of devices attached


APPIUM CONFIGURATION
ANDROID_HOME      /Users/rene.cortes/Library/Android/sdk
JAVA_HOME              /Library/Java/JavaVirtualMachines/jdk-11.0.16.1.jdk/Contents/Home

ANDROID STUDIO es donde creamos el virtual device
We need to launch the application on the emulator and then run the command below
Con este comando obtenemos la info de appPakage  y appActivity, en el apartado de obscurrentwindow
 adb shell dumpsys window windows

La primera parte hasta el / corresponde a appPackage y la segunda corresponde a appActivity
mObscuringWindow=Window{5f10c43 u0 com.code2lead.kwad/com.code2lead.kwad.MainActivity}


Instalar npm install -g appium  si hay algún problema con permisos en Mac ejecutamos:
Sudo chown -R $USER /ysr/local/lib/node_modules

Note
If you facing below error while executing the code then add the args as shown in below solution.

"Appium server has started but is not listening on /status within 60000ms timeout. Make sure proper values have been provided to --base-path, --address and --port process arguments."

Solution:

Add the args as shown below.
appium_service.start(args=['--base-path', '/wd/hub'])

For more information see the link https://github.com/appium/python-client/issues/775



APP.apk installation

To install the app we need to:
* Create virtual device
* Launch virtual device
* Confirm we have device, on terminal execute adb devices, we should see a device running
* Go to Settings > About emulated device > Scroll down to Build Number > Click 7 times on it until we activate developer functionality “This will enable Developer options on the device”
* Go to Settings > System > Advanced > Developer Options > Scroll down to DEBUGGING section and enable USB debugging
* Download the app.apk
* On terminal execute adb install /path/to/app.apk
* Application should be installed on our device

CONFIGURE SERVER
Host 0.0.0.0
Port 4723

CONFIGURE APPIUM INSPECTOR
* Remote Host 127.0.0.1
* Remote Path /wd/hub
* Remote Port 4723

JSON REPRESENTATION
{
  "platformName": "Android",
  "automationName": "UiAutomator2",
  "PlatformVersion": "10",
  "deviceName": "Pixel 3XL",
  "app": "/Users/rene.cortes/Downloads/Android_Demo_App.apk",
  "appPackage": "com.code2lead.kwad",
  "appActivity": "com.code2lead.kwad.MainActivity"
}

To get the udid we execute command adb devices udid is the one in black letters
rene.cortes@WIZELINE Downloads % adb devices
List of devices attached
emulator-5554	device

To get the appPackage and appActivity we execute command adb shell dumpsys window windows
Left side from the “/“ is appPackage and right side is appActivity

mObscuringWindow=Window{ae9a967 u0 com.code2lead.kwad/com.code2lead.kwad.MainActivity}


ISSUES:
When an server issue is faced we can try to resolve it running below commands:
adb uninstall io.appium.settings
adb uninstall io.appium.uiautomator2.server adb uninstall io.appium.uiautomator2.server.test

HYBRID TEST

1.- We can open the web page directly on chrome and search for the elements
Open app in mobile
Open chrome browser and search for chrome://inspect/#devices, this will open the interface between mobile app and web UI view

IOS
{
  "platformName": "iOS",
  "automationName": "XCUITest",
  "PlatformVersion": "16.2",
  "deviceName": "iPhone 11 Pro",
  "app": "/Users/rene.cortes/Desktop/UIKitCatalog-iphonesimulator.app",
  "udid": "C3B2BB2F-09E9-4361-8804-1194E390FB68"
}


RUN TESTS IN IOS
Navigate to https://github.com/appium/ios-uicatalog
Download .zip file 
Unzip file
Enter folder  iOS-uicatalog-master > UICatalog > double click UICatalog.xcodeproj
Project should be opened in xcode
Click on the play arrow to build the project “Device Simulator should be opened”

UDID OF IOS SYSTEMS
From Xcode: Window -> Devices and Simulators -> Simulators. The Identifier value is the UDID.

iOS ISSUE XCODE 65
If we face this issue we need to:
* Launch device
* download the webdriveragent from https://github.com/appium/WebDriverAgent
* Then open a terminal on this folder
* Execute this command to get device information such as deviceName, and did
xcrun simctl list | egrep '(Booted)'

* Then set that information in this terminal with our device information on it, this will install webdriveragent on it, once we see the webdriveragent installed on our device we can launch our app from inspector of from code.

xcodebuild build-for-testing test -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "platform=iOS Simulator,name=iPhone 11 Pro,OS=16.2" IPHONEOS_DEPLOYMENT_TARGET=16.2 GCC_TREAT_WARNINGS_AS_ERRORS=0 COMPILER_INDEX_STORE_ENABLE=NO CODE_SIGNING_ALLOWED=NO

* Execute our script or launch from inspector

NOTES:
In iOS the accessibilityID and name attributes are the same as ID


Finder > Applications > Appium Server GUI > right click > Show Package Contents > Content > Resources > app > node_modules > appium > node_modules > appium-webdriveragent > double click on WebDriverAgent.xcodeproj



ALLURE REPORTS
1.- We need to install on pycharm allure-pytest
2.- goto https://docs.qameta.io/allure/
3.- goto section Manual installation click on Maven Central link https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/
Si nos da error escribimos al inicio de la url https://
4.- Tomar la versión más reciente y descargar el zip file
5.- extraemos el archivo y dentro tenemos un .bat dentro del folder bin
6.- Setear en las variables de entorno el folder bin
* Abrimos una terminal y ejecutamos sudo vim ~/.zshrc
* Luego hacemos click en i  para comenzar a escribir dentro del archivo, y escribimos lo siguiente: export PATH=$PATH:/Users/rene.cortes/Downloads/allure/bin
7.- Salimos y guardamos los cambios del archivo con los siguientes comandos ESC + :wq! + enter
8.- ejecutamos en la terminal allure --version y nos debería de mostrar la version de allure que instalamos


CORRER TESTS Y GENERAR LOS REPORTES

9.- para correr los tests y generar los reportes ejecutamos el siguiente comando
py.test --alluredir='/Users/rene.cortes/Desktop/COPPELReports' -s -v --reruns 1 --reruns-delay 2 RerunTestsPytest/ReRunningFailedTests.py


10.- Para abrir el reporte en formato HTML ejecutamos el siguiente comando
allure serve /Users/rene.cortes/Desktop/COPPELReports




PARALLEL TESTING
To run parallel testing we need to follow below instructions
1.- pip install pytest-xdist
2.- Add udid and systemPort in desired capabilities
3.- Run the file using command as: pytest -n <numOfProcesses>


BADB COMMANDS
Adb devices
Adb install path/of/the/app/to/install
Adb shell dumpsys window windows “search for this mObscuringWindow=Window{863474e u0 com.code2lead.kwad/com.code2lead.kwad.MainActivity} the lest side of the / is the package name com.code2lead.kwad, the right side is the activity name com.code2lead.kwad.MainActivity.
To uninstall an app we need the package name and then
Adb uninstall packageName
Adb kill-server to finish server process
Adb start-server to start server again
Adb shell screen cap -p pathToSaveScreenshot/nameOfScreenshot.png adb shell screencap -p /sdcard/code2lead.png

To take out a file to our pc
adb pull /sdcard/code2lead.png /Users/rene.cortes/Desktop/AppiumCourse/  we need to be on our user, not into the shell

To send a file into virtual device, first is our pc path and second path is where we want to save the file on our virtual device
adb push /Users/rene.cortes/Desktop/AppiumCourse/code2lead.png /sdcard/

To record device screen 
 adb shell screenrecord /sdcard/code2lead.mp4 --size 640x480



ENABLE DEVELOPER OPTIONS

Go to settings > about phone > build number > tap 7 to 10 times on build number until you see a message that developer options has been enabled.

ENABLE COORDINATES ON ANDROID DEVICE
Goto settings > system > advanced > developer options > enable pointer location

FOR THE BOOTCAMP
SERVICE
[
        'appium',
        {
          args: {
            address: 'localhost',
            port: 4723
          },
          //logPath: './'
        }
      ]


pkill -9 Simulator && pkill -9 simulator && sleep 5 && pkill -9 Xcode && pkill -9 xcode && open -a Simulator --args -CurrentDeviceUDID C3B2BB2F-09E9-4361-8804-1194E390FB68  && sleep 15 && cd /Users/rene.cortes/Downloads/WebDriverAgent-4.9.0 && xcodebuild build-for-testing test -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "platform=iOS Simulator,name=iPhone 11 Pro,OS=16.2" IPHONEOS_DEPLOYMENT_TARGET=16.2 GCC_TREAT_WARNINGS_AS_ERRORS=0 COMPILER_INDEX_STORE_ENABLE=NO CODE_SIGNING_ALLOWED=NO && sleep 60 &

mObscuringWindow=Window{668229e u0 com.harley_davidson.ride_planner/com.harleydavidson.rideplanner.onboarding.WelcomeActivity}

mObscuringWindow=Window{447a0c0 u0 com.harley_davidson.ride_planner/com.harleydavidson.rideplanner.onboarding.WelcomeActivity}
