## What is this project?
This is a tool for VFX artists in which it creates USD (.usda) assets and organises them into subfolders. It automatically handles version numbers so you know exactly what version you are currently working on and it has a GUI so artists don't need to use the terminal

## Why did I make it?
I built this because I wanted to understand how real VFX studios manage their asset pipelines. Coming from the world of film and production, I understand how important it is to keep organized especially when working on big projects and artists need a reliable way to store and organise assets without managing folder structures and version numbers. Without a tool like this, assets can get lost and artists could end up working on outdated versions of an asset. This system aims to solve those problems in a simple and accessible way.

## how to install and run it:
1. install python (https://www.python.org/downloads/)
2. download the vfx-pipeline zipfile from github (extract it to your Desktop)
3. open PowerShell
4. run pip install usd-core
5. run pip install PySide6
6. run cd C:\Users\(your user name)\Desktop\vfx-pipeline
7. run 'python app.py' a window should pop up prompting you with a response
8. fill out the fields and click 'Create Asset'
9. your subfolders and .usda file will be created

## What it currently does:
1. Opens a GUI
2. Only allows the user to select either a Character, Prop, or Environment as the asset type
3. Creates a folder with subfolders based on the type and name of the asset
4. Creates a properly structured USD file complete with the asset name the kind it is aswell as what version it is
5. Automatically creates updated versions of the same asset and lists it

> A standalone executable for non-technical users is planned for a future release.
