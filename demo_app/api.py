def test():
    print("hello world")

def another_test():
    print("another change")

@frappe.whitelist()
def test_test():
    print("change")
