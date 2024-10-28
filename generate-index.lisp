


(ql:quickload :spinneret)
(use-package 'spinneret)

(ql:quickload :cl-interpol)
(named-readtables:in-readtable :interpol-syntax)

(defun generate-index ()
(with-html-string
    (:doctype)
    (:html
     (:head
      (:title "Index files")
      )
     (:body
    (:h1 "List of files")
    (:ul
     (:li (:tag :name "a" :attrs (list :href "0.html") "0.html"))
     (:li (:a :href "binomials.html" "bionomial update calculations"))
     (:li (:a :href "0.html" "dxf example file"))
     )
    )
   )))

(defun write-string-to-file (fname string)
  (with-open-file (str fname
    :direction :output
    :if-exists :supersede
    :if-does-not-exist :create)
  (format str "~a" string)))

(write-string-to-file
 "~/projects/philnik.github.io//test-generate-index.html"
 (generate-index))





(let ((link "1.html"))
(with-html
  (:span "Here is some copy, with "
    (:a :href link "a link."))))
