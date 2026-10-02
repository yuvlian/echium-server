@echo off
cls
echo dont worry it's running.

uv run protoc.exe -I . --fasterproto2_out=./proto StarRail.proto

if not exist ".\common\res\avatarConfigs.json" (
    echo avatarConfigs.json is missing. downloading...
    uv run update_res.py
) else (
    echo.
    choice /M "do you want to update avatarConfigs.json"

    if errorlevel 2 (
        echo skipping avatarConfigs.json update.
    ) else (
        uv run update_res.py
    )
)
