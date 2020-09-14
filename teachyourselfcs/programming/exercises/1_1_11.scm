#lang scheme

; the recursive version is pretty simple:

(define (f-rec n)
  (cond ((< n 3) n)
  (else (+ (f-rec (- n 1))
           (* 2 (f-rec (- n 2)))
           (* 3 (f-rec (- n 3)))))))
           
           
; the iterative version (even though I'd rather solve it in a different way):

(define (f-iter n)
  (define (iter n a b c)
    (if (<= n 0)
      a
      (iter (- n 1) b c (+ (* 3 a) (* 2 b) c))))
  (if (< n 3)
    n
    (iter n 0 1 2)))


; tests:

(f-rec -1)
(f-iter -1)

(f-rec 2)
(f-iter 2)

(f-rec 3)
(f-iter 3)

(f-rec 5)
(f-iter 5)

(f-rec 10)
(f-iter 10)
