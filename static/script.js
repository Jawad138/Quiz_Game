document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault();  // Prevent the default form submission

        // Gather all the selected answers
        const formData = new FormData(form);
        const questionCount = document.querySelectorAll('.question').length;
        let allQuestionsAnswered = true;

        // Check if each question has been answered
        for (let i = 0; i < questionCount; i++) {
            if (!formData.has(`question_${i}`)) {
                allQuestionsAnswered = false;
                break;
            }
        }

        if (allQuestionsAnswered) {
            // If all questions are answered, submit the form
            form.submit();
        } else {
            alert("Please answer all the questions before submitting.");
        }
    });
});
