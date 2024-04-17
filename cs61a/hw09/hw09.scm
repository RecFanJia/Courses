(define (curry-cook formals body)
  (if (null? (cdr formals))  ; Check if there is only one more formal left
      `(lambda (,(car formals)) ,body)  ; Create a lambda with one formal and the body
      `(lambda (,(car formals)) ,(curry-cook (cdr formals) body))  ; Recurse and nest lambdas
  ))

(define (curry-consume curry args)
  (if (null? args) 
  curry
  (curry-consume (curry (car args)) (cdr args))
  ))

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map (lambda (option)
               (cons (list 'equal? (car (cdr switch-expr)) (car option)) (cdr option)))
             (car (cdr (cdr switch-expr))))))
