# Configure new system

This repo will help init your system after fresh install.

## Start on new system
```
git clone git@github.com:Tutkovics/configuration.git

cat << EOF >> $HOME/.bashrc
# Add custom aliases
source $HOME/configuration/aliases/aliases.txt
source $HOME/configuration/aliases/git_aliases.txt

alias tmux='tmux -f $HOME/configuration/dots/.tmux.conf'
EOF
```

Use bookmarks feature. 
```
# e.g., create new bookmark
ln -s ~/configuration/ .bookmarks/@configuration 
```
