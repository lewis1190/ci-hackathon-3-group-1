document.getElementById('editItemModal').addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const itemId = button.getAttribute('data-item-id');
    const itemText = button.getAttribute('data-item-text');
    
    document.getElementById('editItemId').value = itemId;
    document.getElementById('itemText').value = itemText;
});

// Prevent checkbox default behavior and submit form instead
document.querySelectorAll('button[type="submit"] .form-check-input').forEach(checkbox => {
    checkbox.addEventListener('click', function (event) {
        event.preventDefault();
        event.stopPropagation();
        this.disabled = true;
        this.closest('button').disabled = true;
        this.closest('button').closest('form').submit();
    });
});

// Disable buttons on form submit to prevent double-requests
const formsToProtect = [
    '/toggle-item/',      // Mark Complete / Toggle
    '/delete-item/',      // Delete task
    '/delete-list/',      // Delete list
    '/clear-completed/'   // Clear Completed Tasks
];

formsToProtect.forEach(formAction => {
    document.querySelectorAll(`form[action*="${formAction}"]`).forEach(form => {
        form.addEventListener('submit', function(event) {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.style.opacity = '0.6';
                submitBtn.style.cursor = 'not-allowed';
            }
            
            // For task-related actions, disable all buttons in the task item
            if (formAction === '/toggle-item/' || formAction === '/delete-item/') {
                const taskItem = this.closest('li');
                if (taskItem) {
                    taskItem.querySelectorAll('button').forEach(btn => {
                        btn.disabled = true;
                        btn.style.opacity = '0.6';
                        btn.style.cursor = 'not-allowed';
                    });
                }
            }
        });
    });
});
