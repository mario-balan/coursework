#lang scheme

; the new-if structure doesn't have the property of evaluating only one of its consequents because it operates as a procedure.
;
; both 'then-clause' and 'else-clause' are evaluated/expanded before 'predicate' is applied.
;
; - in the case of:

(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x)
                 x)))
;
; - the 'then-clause' is 'guess', which is not a problem.
;
; - the 'else-clause' is '(sqrt-iter (improve guess x) x)'.
;
; - which calls 'sqrt-iter' again.
; - which calls 'new-if' again.
; - and so on...
;
; and the stack overflows.
