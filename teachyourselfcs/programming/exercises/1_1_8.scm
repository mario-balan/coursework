#lang scheme

(define (cbrt-iter guess x)
    (if (good-enough? guess x)
          guess
	        (cbrt-iter (improve guess x) x)))

; searching for other answers to 1.1.7 I discovered that:
; if you iterate until guess and next guess are equal
; you can get an answer to the limit of system precision.
; like this:

(define (good-enough? guess x)
    (= (improve guess x) guess))

;this is the only procedure that was changed
;the previous 'average' procedure was discarded
(define (improve guess x)
    (/ (+ (/ x (square guess)) (* 2 guess)) 3))

(define (square x) (* x x))

(define (cbrt x)
    (cbrt-iter 1.0 x))

; for helping with tests:

(define (cube x)(* x x x))

; tests:
(cbrt 8)
(cbrt (cube 10))
