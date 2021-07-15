" General
syntax on               " Enable syntax highlighting
colorscheme darkblue    " Change default color scheme
set  number	        " Show line numbers
set linebreak	        " Break lines at word (requires Wrap lines)
set showbreak=+++	" Wrap-broken line prefix
set textwidth=100	" Line wrap (number of cols)
set showmatch	        " Highlight matching brace
set spell	        " Enable spell-checking
set visualbell	        " Use visual bell (no beeping)
 
set hlsearch	        " Highlight all search results
set smartcase	        " Enable smart-case search
set ignorecase	        " Always case-insensitive
set incsearch	        " Searches for strings incrementally
 
set autoindent	        " Auto-indent new lines
set expandtab	        " Use spaces instead of tabs
set shiftwidth=4	" Number of auto-indent spaces
set softtabstop=4       " Remove 4 spaces with one Backspace
set smartindent	        " Enable smart-indent
set smarttab	        " Enable smart-tabs
set softtabstop=4	" Number of spaces per Tab
 
" Advanced
set ruler       	" Show row and column ruler information
 
set undolevels=1000 	" Number of undo levels
set backspace=indent,eol,start	" Backspace behaviour
set showcmd             " show command in bottom bar
set cursorline          " highlight current line
set wildmenu            " visual autocomplete for command menu
set lazyredraw          " redraw only when we need to
set foldenable          " enable folding

" Backup function
set backup
set backupdir=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set backupskip=/tmp/*,/private/tmp/*
set directory=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set writebackup
