#lang scheme

; - the tolerance of 0.001 is naturally not sensitive enough when dealing with numbers equal or smaller than the value itself (e.g. 0.001, 0.0001):

(sqrt 0.001)
; 0.04124542607499115

(* 0.04124542607499115 0.04124542607499115)
; 0.0017011851721075596

(sqrt (* 0.01 0.01))
; 0.03230844833048122

; - as for large numbers, there may not be enough decimals for floating-point numbers to reach the tolerance threshold, so 'good-enough?' will always evaluate to #f (entering an infinite loop):

(sqrt 1e10)
; 100000.0

(sqrt 1e11)
; 316227.7660168379

(sqrt 1e12)
; 1000000.0

;(sqrt 1e13)
; . . user break <---- process was hanging (infinite loop).



; - as 'rate of change' is defined by |(x1 - x0) / x0|, where x1 is the next guess and x0 is the previous guess.
;
; - we can:
;     (a) look forward for the next guess ('improve guess') inside the 'good-enough?' procedure and compare it to 'guess' to decide if 'sqrt-iter' will evaluate it or not;
;     OR
;     (b) look backwards, creating a variable 'old-guess' in 'sqrt-iter'. this way we won't need to evaluate 'improve guess' when checking 'good-enough?'.
;
; - going with (a) only minor changes to the original code are needed:

(define (good-enough? guess x)
  (< (abs (/ (- (improve guess x) guess) guess)) 0.001))

; which does work a lot better for smaller and larger numbers.


; here is the complete code:

(define (sqrt-iter guess x)
    (if (good-enough? guess x)
          guess
	        (sqrt-iter (improve guess x) x)))

(define (good-enough? guess x)
    (< (abs (/ (- (improve guess x) guess) guess)) 0.001))

(define (improve guess x)
    (average guess (/ x guess)))

(define (average x y)
    (/ (+ x y) 2))

(define (square x) (* x x))

(define (abs x)
    ((if (> x 0) + -) x))

(define (sqrt x)
    (sqrt-iter 1.0 x))

; and here are some tests:
(sqrt (* 0.01 0.01))
(sqrt 1e13)
