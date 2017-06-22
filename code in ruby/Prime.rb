puts "***Calculate Prime Number***"
def prime(n)
  is_prime = true
  for i in 2..Math.sqrt(n)
    if n % i == 0
      is_prime = false
    end
  end
  if is_prime
    puts "#{n} is prime!"
  else
    puts "#{n} is not prime."
  end
end
puts "enter number for check: "
  n = gets
  n = n.to_i

prime(n)