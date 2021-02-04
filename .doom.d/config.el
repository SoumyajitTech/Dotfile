(add-to-list 'load-path "/usr/local/share/emacs/site-lisp/mu4e")

(setq doom-font (font-spec :family "monospace" :size 14 :weight 'semi-light)
       doom-variable-pitch-font (font-spec :family "sans" :size 13))

(setq doom-theme 'doom-dracula)

(setq org-directory "~/org/")

(setq display-line-numbers-type t)
(global-set-key "\C-x\ t" 'toggle-truncate-lines)

(setq browse-url-browser-function 'eww-browse-url)

(setq neo-window-fixed-size nil)

(require 'magit)

(defun prefer-horizontal-split ()
  (set-variable 'split-height-threshold nil t)
  (set-variable 'split-width-threshold 40 t)) ; make this as low as needed
(add-hook 'markdown-mode-hook 'prefer-horizontal-split)

(map!
  (:after dired
    (:map dired-mode-map
     "C-x i" 'peep-dired
     )))
(evil-define-key 'normal peep-dired-mode-map (kbd "j") 'peep-dired-next-file
                                             (kbd "k") 'peep-dired-prev-file)
(add-hook 'peep-dired-hook 'evil-normalize-keymaps)

(custom-set-variables
 '(elfeed-feeds
   (quote
    (("https://www.reddit.com/r/linux.rss" reddit linux)
     ("https://www.gamingonlinux.com/article_rss.php" gaming linux)
     ("https://hackaday.com/blog/feed/" hackaday linux)
     ("https://opensource.com/feed" opensource linux)
     ("https://linux.softpedia.com/backend.xml" softpedia linux)
     ("https://itsfoss.com/feed/" itsfoss linux)
     ("https://www.zdnet.com/topic/linux/rss.xml" zdnet linux)
     ("https://www.phoronix.com/rss.php" phoronix linux)
     ("http://feeds.feedburner.com/d0od" omgubuntu linux)
     ("https://www.computerworld.com/index.rss" computerworld linux)
     ("https://www.networkworld.com/category/linux/index.rss" networkworld linux)
     ("https://www.techrepublic.com/rssfeeds/topic/open-source/" techrepublic linux)
     ("https://betanews.com/feed" betanews linux)
     ("http://lxer.com/module/newswire/headlines.rss" lxer linux)
     ("https://distrowatch.com/news/dwd.xml" distrowatch linux))))
 '(package-selected-packages
   (quote
    (exwm peep-dired nav-flash evil-mu4e elfeed))))
