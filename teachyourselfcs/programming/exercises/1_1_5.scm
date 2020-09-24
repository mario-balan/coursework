#lang scheme

(define (p) (p))

(define (test x y)
  (if (= x 0)
    0
    y))

; - applicative-order:
;
; (test 0 (p)) never finishes evaluating because (p) will always expand to (p).


; - normal-order:
; evaluates to 0 ((p) is never expanded), like this:
;
; (test 0 (p))
; (if (= 0 0) 0 (p))
; (if #t 0 (p))
; 0
