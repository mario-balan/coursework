#lang scheme

; finding specific numbers of a Pascal triangle given a row and a column
; for some interesting stuff, I'd recommend checking 'Pascal's Triangle - Numberphile'
; on youtube.com


; first row is (0,0)

(define (pascal row col)
  (if (or (= col 0) (= col row))
    1
    (+ (pascal (- row 1) (- col 1)) (pascal (- row 1) col))))

; an example of expansion (computing (pascal (4, 2)):
; (pascal 4 2)
; (+ (pascal 3 1) (pascal 3 2))
; (+ (+ (pascal 2 0) (pascal 2 1)) (+ (pascal 2 1) (pascal 2 2)))
; (+ (+ (pascal 2 0) (+ (pascal 1 0) (pascal 1 1))) (+ (+ (pascal 1 0) (pascal 1 1)) (pascal 2 2)))
; (+ (+ 1 (+ 1 1)) (+ (+ 1 1) 1))

; printing the first 6 rows:
(printf "~a\n" (pascal 0 0))
(printf "~a ~a\n" (pascal 1 0) (pascal 1 1))
(printf "~a ~a ~a\n" (pascal 2 0) (pascal 2 1) (pascal 2 2))
(printf "~a ~a ~a ~a\n" (pascal 3 0) (pascal 3 1) (pascal 3 2) (pascal 3 3))
(printf "~a ~a ~a ~a ~a\n" (pascal 4 0) (pascal 4 1) (pascal 4 2) (pascal 4 3) (pascal 4 4))
(printf "~a ~a ~a ~a ~a ~a\n" (pascal 5 0) (pascal 5 1) (pascal 5 2) (pascal 5 3) (pascal 5 4) (pascal 5 5))
