# select area copy to clippboard and save file
DIR="/home/tutkovics/Pictures/Screenshot"
FILE=$(date +"Screenshot_%Y-%m-%d_%H-%M-%S.png")
FULLFILE=$DIR/$FILE
gnome-screenshot --area --delay=0 --file=$FULLFILE
#--clipboard not works with save function
# Copy to clipboard:
xclip -selection clipboard -t image/png -i $FULLFILE
