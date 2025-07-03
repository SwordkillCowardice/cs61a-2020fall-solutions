(define (split-at lst n)
  (define (reverse ls cur_ls)
    (if (null? ls) cur_ls (reverse (cdr ls) (cons (car ls) cur_ls)))
  )
  (define (split_helper cur_lst res_lst cur_len)
    (cond ((or (= cur_len n) (and (< cur_len n) (null? res_lst))) (cons (reverse cur_lst nil) res_lst))
          ((and (< cur_len n) (not (null? res_lst))) 
          (split_helper (cons (car res_lst) cur_lst) (cdr res_lst) (+ 1 cur_len)))
    )
  )
  (split_helper nil lst 0)
)


(define (compose-all funcs)
  (define (final x) (if (null? funcs) x 
  ((compose-all (cdr funcs)) ((car funcs) x))))
  final
)