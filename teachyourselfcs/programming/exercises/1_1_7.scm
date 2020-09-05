;Exercise 1.1.7:

; complete code 
; refer to ./1_1_7.txt for commentary on this answer

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

; Tests:
(sqrt (* 0.01 0.01)) 
(sqrt 1e13)
