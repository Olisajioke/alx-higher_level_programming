-- Check if the database exists before attempting to delete it
DO $$ 
BEGIN
    IF (SELECT COUNT(*) FROM information_schema.schemata WHERE schema_name = 'hbtn_0c_0') > 0 THEN
        -- Database exists, so drop it
        DROP DATABASE hbtn_0c_0;
    END IF;
END $$;
