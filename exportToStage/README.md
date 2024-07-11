Required Steps:


1.  Create RSA keypair file:
   
       Command Line:<br>
           openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
           openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub

       In Notebook:<br>
          Add private key file (rsa_key.p8) to your notebook directory
    
       In Snowflake, with contents of rsa_key.pub file:<br>
           alter user <my_user> set rsa_public_key='MIIBIjANBgkqh...';
    
3.  Edit creds.json file to match your Snowflake account and credentials
   
4.  Ensure you have Snowflake setup, with access to an External/Internal Stage and the tables/data you want to export
