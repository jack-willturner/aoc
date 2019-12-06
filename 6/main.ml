open List

let rec search
          graph
          expand
          fringe
          goal
          strategy
          visited
  = match fringe with
  | []    -> failwith "No path"
  | x::xs ->
     if goal x then x
     else search graph expand (strategy xs (expand x graph) (x::visited)) goal strategy (x::visited);;

let map =
  [ ('A','Z',75);
    ('A','S',100);
    ('B','Z',10)];;

let rec expand vertex graph =
  match graph with
  | [] -> []
  | (v1,v2,_)::xs ->
     if v1 = vertex then (v2::expand vertex xs)
     else if v2 = vertex then (v1::expand vertex xs)
     else expand vertex xs;;

let rec remove fromls ls = match fromls with
  | [] -> []
  | x::xs -> if mem x ls then (remove xs ls) else (x :: remove xs ls)

let strategy oldf newf visited = remove (newf @ oldf) visited;;

search map expand ['B'] (fun x -> x ='A') strategy;;
