FROM python:alpine
RUN apk update \
    && apk add --no-cache git curl zsh stow tmux vim less mc tree
RUN curl -Lo omz-install.sh https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh \
    && CHSH=no RUNZSH=no sh omz-install.sh --unattended
RUN git clone https://github.com/mindthump/dotfiles.git ~/.dotfiles \
    && rm -f ~/.zshrc omz-install.sh \
    && stow --dir ~/.dotfiles --stow zsh