def mask_email(email_address):
    local = email_address.index('@')
    if len(email_address[:local]) <= 64 and len(email_address[local+1:]) <= 255:
        valid_email = email_address
    replaced_email = '*'*len(valid_email[:local]) + valid_email[local:]
    return replaced_email

print(mask_email("angie@mail.com"))