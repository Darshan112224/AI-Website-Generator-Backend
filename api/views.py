import torch
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Initialize logger
logger = logging.getLogger(__name__)

# Model name
MODEL_NAME = "bigcode/starcoder2-15b"

# Check if CUDA (GPU) is available
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Using device: {device}")

try:
    logger.info(f"Loading model: {MODEL_NAME}")

    # Use pipeline for easy text generation
    pipe = pipeline("text-generation", model=MODEL_NAME, device=0 if torch.cuda.is_available() else -1)

    # Load tokenizer (separately if needed)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error("Failed to load model: %s", str(e))
    raise e


@api_view(['POST'])
def generate_website(request):
    """
    API endpoint to generate website code using StarCoder2-15B.
    """
    try:
        description = request.data.get('description')
        tech_stack = request.data.get('tech_stack', 'React.js')

        if not description:
            return Response({'message': 'Description is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Improved prompt for better results
        prompt = (f"""
                  ### Instruction: Generate a fully functional {tech_stack} website.
                  - Include a well-structured HTML file.
                  - Write clean and responsive CSS.
                  - Implement JavaScript functionality.
                  - Format the output properly.

                  ### Website Description:
                  {description}

                  ### Code Output:
                  """

        )

        logger.info("Generating website code for description: %s", description)

        # Use pipeline for generation
        generated_output = pipe(
            prompt,
            max_length=2048,  # Limit output length
            temperature=0.7,   # Adjust randomness
            top_p=0.95,        # More diverse sampling
            do_sample=True,
            return_full_text=False  # Prevents prompt repetition in output
        )

        generated_code = generated_output[0]["generated_text"]

        logger.info("Generated Code: %s", generated_code)

        if not generated_code.strip() or len(generated_code) < 50:  # Threshold for valid output
            return Response(
                {'message': 'No valid code was generated. Try refining your description or using a different tech stack.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    except Exception as e:
        logger.error("Error generating website: %s", str(e))
        return Response({'message': 'Internal server error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
