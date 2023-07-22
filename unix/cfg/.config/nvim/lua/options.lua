vim.cmd("filetype off")
vim.cmd("filetype plugin indent on")
vim.cmd("set clipboard+=unnamedplus")

vim.opt.relativenumber=true
vim.opt.number=true

-- or light if you want light mode
vim.opt.background="dark"
vim.cmd("colorscheme gruvbox")

-- Better display for messages
vim.opt.cmdheight = 2
-- You will have bad experience for diagnostic messages when it's default 4000.
vim.opt.updatetime=300
vim.opt.shortmess = vim.opt.shortmess + "c"

-- http://stackoverflow.com/questions/2158516/delay-before-o-opens-a-new-line
vim.opt.timeoutlen=300
vim.opt.scrolloff=2
vim.opt.showmode=false

-- I wanna check how not having these three works out..
-- set hidden
-- set nojoinspaces
-- set nowrap

-- Set space as the mapleader
-- nnoremap <SPACE> <Nop>
-- "let mapleader=" "

-- Always draw sign column. Prevent buffer moving when adding/deleting sign.
vim.opt.signcolumn="yes"
-- Sane splits
vim.opt.splitright=true
vim.opt.splitbelow=true

-- Permanent undo
vim.opt.undofile=true

-- Decent wildmenu
vim.opt.wildmode="list:longest"
vim.opt.wildignore={
  ".hg", ".svn" ,"*~", "*.png","*.jpg","*.gif","*.settings",
  "Thumbs.db","*.min.js","*.swp,publish/*","intermediate/*",
  "*.o","*.hi","Zend","vendor" 
}

-- Tab options
vim.opt.shiftwidth=2
vim.opt.softtabstop=2
vim.opt.tabstop=2
vim.opt.expandtab=true

-- Wrapping options
-- tc: wrap text and comments using textwidth
-- r: continue comments when pressing ENTER in I mode
-- q: enable formatting of comments with gq
-- n: detect lists for formatting
-- b: auto-wrap in insert mode, and do not wrap old long lines
-- Try defaults before adding/using r and b
vim.cmd("set formatoptions+=n")

-- Proper search
vim.opt.incsearch=true
vim.opt.ignorecase=true
vim.opt.smartcase=true
vim.opt.gdefault=true

-- Remove toolbar
vim.cmd("set guioptions-=T")
vim.opt.colorcolumn="80,100"

