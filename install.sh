#!/bin/bash
mkdir ~/.moony_app
cp -r ./moony ~/.moony_app/
homepath=$HOME
echo "Icon=$HOME/.moony_app/fmoon.png" >> "Moony Creator"
cp ./moony/images/fmoon.png ~/.moony_app
cp "Moony Creator" ~/.moony_app/ ~/Desktop/