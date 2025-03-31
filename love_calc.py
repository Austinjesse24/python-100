def calculate_love_score(name1, name2):
    # Combine both names
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of letters in "TRUE"
    t_count = combined_names.count('t')
    r_count = combined_names.count('r')
    u_count = combined_names.count('u')
    e_count = combined_names.count('e')
    
    # Calculate TRUE total
    true_total = t_count + r_count + u_count + e_count
    
    # Count occurrences of letters in "LOVE"
    l_count = combined_names.count('l')
    o_count = combined_names.count('o')
    v_count = combined_names.count('v')
    e_count = combined_names.count('e')  
    # We already counted 'e' above, but counting again for clarity
    
    # Calculate LOVE total
    love_total = l_count + o_count + v_count + e_count
    
    # Combine to make 2-digit number
    love_score = int(str(true_total) + str(love_total))
    
    return love_score

# Test with the example
print(calculate_love_score("roberta", "ethan"))