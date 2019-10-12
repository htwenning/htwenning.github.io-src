```clojure
(ns clojureclass.core
	(:gen-class
	:methods [[methoda [] void]
		^:static [methodb [] void]]
	))
	
(defun -methoda
""
[this]
(println "methoda"))

(defun -methodb
""
[]
(println "methodb static"))

```

