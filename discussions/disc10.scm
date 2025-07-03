; Q1 a 3 b #t

; Q2 1 -96

; Q3
(define (factorial x)
    (if (<= x 1) 1 (* x (factorial (- x 1))))
)

; Q4
(define (fib n)
    (if (< n 2) n (+ (fib (- n 1)) (fib (- n 2))))
)

;Q5 自己写的
; (define (my-append a b)
;     (if (equal? nil (cdr a)) (cons (car a) b) (cons (car a) (my-append (cdr a) b)))
; )

;Q5 官答
(define (my-append a b)
    (if (null? a) b (cons (car a) (my-append (cdr a) b)))
)

; Q6
; 第一个定义了一个变量x,第二个定义了一个过程x,该过程为零参数过程
(define s '(5 4 (1 2) 3 7))
(car (cdr (cdr (cdr s))))

; Q7
(define (duplicate lst)
    (if (null? lst) nil (cons (car lst) (cons (car lst) (duplicate (cdr lst)))))
)

; Q8
(define (insert element lst index)
    (if (= index 0) (cons element lst) (cons (car lst) (insert element (cdr lst) (- index 1))))
)