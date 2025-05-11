@echo off
set goAgain="0"
set file=%1

:start

if "%goAgain%"=="1" (
    set file=""
)

if "%file%"=="" (
    set /p file="Please input a file path: "
)

for %%a in ("%file:*.=%") do set "fileExtension=%%a"

:tryAgain
if /I "%fileExtension%" in ["png","jpeg","jpg"] (
    echo "This is an image. Would you like to:"
    echo "1. Decode (extract data embedded in the image)"
    echo "2. Double Encode (embed data into this image)"
    set /p doubleEncode=""
    if "%doubleEncode%"=="1" (
        ".\scripts\Img2File.py" "%file%"
        if errorlevel 1 (
            echo Error occurred during decoding.
            goto :end
        )
    ) else if "%doubleEncode%"=="2" (
        ".\scripts\File2Img.py" "%file%"
        if errorlevel 1 (
            echo Error occurred during encoding.
            goto :end
        )
    ) else (
        echo "Please enter a valid selection (1 or 2)."
        goto :tryAgain
    )
) else (
    ".\scripts\File2Img.py" "%file%"
    if errorlevel 1 (
        echo Error occurred during encoding.
        goto :end
    )
)

:askAgain
echo.
echo Would you like to convert another file?
echo 0. Quit
echo 1. Convert Another File
set /p goAgain=""
if "%goAgain%"=="1" (
    goto :start
)

:end
echo Thank you for using my program
pause
exit /b 0