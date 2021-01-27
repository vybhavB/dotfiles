call plug#begin('~/.local/share/nvim/plugged')
Plug 'flazz/vim-colorschemes'
Plug 'luochen1990/rainbow'
Plug 'scrooloose/nerdtree'
Plug 'tpope/vim-surround'
Plug 'airblade/vim-gitgutter'
Plug 'lervag/vimtex'
Plug 'shime/vim-livedown'
Plug 'w0rp/ale'
Plug '/usr/local/opt/fzf'
Plug 'junegunn/fzf.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'Yggdroot/indentLine'
Plug 'preservim/nerdcommenter'
" Plug 'yuezk/vim-js'
" Plug 'HerringtonDarkholme/yats.vim'
" Plug 'maxmellon/vim-jsx-pretty'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'OmniSharp/omnisharp-vim'

Plug 'glacambre/firenvim', { 'do': { _ -> firenvim#install(69) } } " Need to have 69 just because it doesn't work without
call plug#end()

autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
" autocmd BufWritePost * NERDTreeFocus | execute 'normal R' | wincmd p
"let g:coc_node_path = '/home/vybhavb/.nvm/versions/node/v12.9.1/bin/node'

"autocmd User Node
"  \ if &filetype == "javascript" |
"  \   nmap <buffer> <C-w>f <Plug>NodeVSplitGotoFile |
"  \   nmap <buffer> <C-w><C-f> <Plug>NodeVSplitGotoFile |
"  \ endif

let g:tex_flavor = 'latex'

" Colors {{
syntax on
set termguicolors
let ayucolor='dark'
colorscheme ayu
" CI Dark
" syntax on
" set termguicolors
" colorscheme ci_dark
" set fillchars+=vert:│
" let g:airline_theme = 'ci_dark'
" let g:lightline = { 'colorscheme': 'ci_dark' }
" }}

let mapleader = " " 
set tabstop=2      " number of visual spaces per TAB
set softtabstop=2   " number of spaces in tab when editing
set shiftwidth=2    " number of spaces to use for autoindent
set expandtab       " tabs are space
set autoindent
"set copyindent      " copy indent from the previous line
set clipboard=unnamedplus
set number relativenumber                   " show line number
set showcmd                  " show command in bottom bar
set wildmenu                 " visual autocomplete for command menu
set showmatch                " highlight matching brace
set laststatus=2           " window will always have a status line
set nobackup
set noswapfile
let &colorcolumn="100,".join(range(120,999),",")
set splitbelow
set splitright
set foldenable
set foldlevelstart=10  " default folding level when buffer is opened
set foldnestmax=10     " maximum nested fold
set foldmethod=syntax  " fold based on indentation

" Resize splits {{{

nnoremap <silent> <Leader>+ :exe "resize " . (winheight(0) * 3/2)<CR>
nnoremap <silent> <Leader>- :exe "resize " . (winheight(0) * 2/3)<CR>

" }}}

" edit/reload vimrc
nmap <leader>ev :e $MYVIMRC<CR>
nmap <leader>sv :so $MYVIMRC<CR>

" better ESC
inoremap jj <esc>

" fast save and close
nmap <leader>w :w<CR>
nmap <leader>x :x<CR>
nmap <leader>q :q<CR>

"" YCM mappings {{{
"nnoremap <leader>t :YcmCompleter GoTo<CR>
" }}}

" YCM {{{
"let g:ycm_server_keep_logfiles = 1
"let g:ycm_server_log_level = 'debug'
"let g:ycm_filetype_specific_completion_to_disable = {
"   "\ 'gitcommit': 1,
"   "\ 'python': 1
"   "\}
"let g:ycm_complete_in_comments = 1
"let g:ycm_complete_in_strings = 1
"let g:ycm_use_ultisnips_completer = 1 " Default 1, just ensure
"let g:ycm_seed_identifiers_with_syntax = 1 " Completion for programming language's

" }}}

" move up/down consider wrapped lines
nnoremap j gj
nnoremap k gk


" nerd tree {{
map <C-n> :NERDTreeToggle<CR>
let NERDTreeShowHidden=1
let NERDTreeIgnore = ['\.pyc$', '__pycache__','/node_modules','/.next']
" }}

" IndentLine {{
"let g:indentLine_char = ''
"let g:indentLine_first_char = ''
let g:indentLine_char_list = ['|', '¦', '┆', '┊']
let g:indentLine_showFirstIndentLevel = 2
let g:indentLine_setColors = 0
" }}
"" Remaps {{

" " Copy to clipboard
"vnoremap  <leader>y  "+y
"nnoremap  <leader>Y  "+yg_
"nnoremap  <leader>y  "+y
"nnoremap  <leader>yy  "+yy

"" " Paste from clipboard
"nnoremap <leader>p "+p
"nnoremap <leader>P "+P
"vnoremap <leader>p "+p
"vnoremap <leader>P "+P

nnoremap <leader>p :tabp<CR>
nnoremap <leader>n   :tabn<CR>
nnoremap <C-t>     :tabnew<CR>

"" }}

" <Ctrl-l> redraws the screen and removes any search highlighting.
nnoremap <silent> <C-l> :nohl<CR><C-l>

"" Ale {{
let g:ale_fixers = {
\   'javascript': ['eslint'],
\}

let g:ale_fix_on_save = 1
"" }}

" FZF
"nnoremap <silent> <leader>f :FZF<cr>
let $FZF_DEFAULT_COMMAND = 'rg --files'
nnoremap <Leader>gf :GFiles<CR>
nnoremap <Leader>f :Files<CR>
nnoremap <Leader>b :Buffers<CR>
nnoremap <Leader>h :History<CR>
nnoremap <Leader>g :Rg<CR>
"nnoremap <C-p> :GFiles

" COC
inoremap <silent><expr> <TAB>
      \ pumvisible() ? coc#_select_confirm() :
      \ coc#expandableOrJumpable() ? "\<C-r>=coc#rpc#request('doKeymap', ['snippets-expand-jump',''])\<CR>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

let g:coc_snippet_next = '<tab>'

nmap <leader>gd <Plug>(coc-definition)
nmap <leader>gr <Plug>(coc-references)

let g:coc_global_extensions = [
  \ 'coc-snippets',
  \ 'coc-pairs',
  \ 'coc-tsserver',
  \ 'coc-eslint',
  \ 'coc-json',
  \ ]

"

" LiveDown
nmap gm :LivedownToggle<CR>

"

" VimTex
"g:vimtex_compiler_progname = 'nvr'
"

"" vim-airline {
let g:airline#extensions#tabline#enabled = 1
"" }
