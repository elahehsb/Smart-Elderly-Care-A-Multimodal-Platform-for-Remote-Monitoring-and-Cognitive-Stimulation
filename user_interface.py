def display_recommendations():
    """Display the latest recommendations for caregivers."""
    recommendations = data[['timestamp', 'recommendation']].tail(5)  # Show last 5 recommendations
    print("Latest Recommendations:")
    print(recommendations.to_string(index=False))

def main():
    while True:
        print("\nElderly Care System")
        print("1. View Latest Recommendations")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_recommendations()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
