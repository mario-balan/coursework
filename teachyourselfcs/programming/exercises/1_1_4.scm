#lang scheme

; the operator will be defined by the IF statement, which will return '+' or '-' (i.e. a + |b|)
;
; in the same manner, it is possible to get an absolute value through:

(define (abs x)
    ((if (> x 0) + -) x)))
