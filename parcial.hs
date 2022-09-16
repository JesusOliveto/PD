import Data.List


conc_lista :: [a] -> [a] -> [a]
conc_lista l1 l2 = foldr (:) l2 l1


init_list :: [a] -> [a]
init_list l = init l


length_list :: [a] -> Int
length_list l = length l


palindromo :: Eq a => [a] -> Bool
palindromo l = l == reverse l



list_may :: Ord a => Int -> [a] -> [a]
list_may n l = take n (reverse (sort l))

