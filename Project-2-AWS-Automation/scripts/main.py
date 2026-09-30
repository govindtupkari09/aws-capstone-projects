def show_menu():
    print("\n==============================")
    print("     AWS RESOURCE AUTOMATOR")
    print("==============================")
    print("1. Create S3 Bucket")
    print("2. Upload File to S3")
    print("3. Launch EC2")
    print("4. List EC2 Instances")
    print("5. Stop EC2 Instance")
    print("6. Terminate EC2 Instance")
    print("7. Exit")


while True:
    show_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        import s3_create_bucket

    elif choice == "2":
        import s3_upload_file

    elif choice == "3":
        import ec2_launch

    elif choice == "4":
        import ec2_list_instances

    elif choice == "5":
        import ec2_stop_instance

    elif choice == "6":
        import ec2_terminate_instance

    elif choice == "7":
        print("\nExiting AWS Resource Automator...")
        break

    else:
        print("\nInvalid choice. Please try again.")