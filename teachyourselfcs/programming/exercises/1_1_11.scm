#lang scheme

; the recursive version is pretty simple:

(define (f-rec n)
  (cond ((< n 3) n)
  (else (+ (f-rec (- n 1))
           (* 2 (f-rec (- n 2)))
           (* 3 (f-rec (- n 3)))))))
