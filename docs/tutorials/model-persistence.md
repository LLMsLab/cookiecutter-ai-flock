# Model output

The best practice for storing binary files for model persistence in
machine learning projects is to use a binary file format such as HDF5,
PyTorch's `.pt` file format, Pickle or Joblib. This allows you to save
the model weights and architecture in a compact and efficient manner,
which can then be loaded and used for prediction or further training.

Here are some additional best practices for storing binary files:

- **Store binary files in a separate directory:** Create a separate
directory (`models`) within your project structure to store binary
files, to keep your code and data organized.
- **Use version control:** Use version control tools like Git to manage
changes to binary files, so that you can revert to previous versions if
necessary.
- **Use cloud/on-premises storage:** Consider using the Data Hub remote
server storage solutions to store binary files, so that they can be
easily shared and accessed by multiple team members or systems.
- **Store metadata:** Store metadata along with the binary file, such as
the training data used to create the model, the parameters used during
training, and the accuracy metrics obtained. This information can be
useful for understanding and reproducing the results.

!!! warning
    If you are Git-tracking the model data, do not include the
    `model_output` directory in the centralized repository. This
    directory must only be placed in the user's data directory.

By following these best practices, you can ensure that your binary files
are stored and managed in a secure, organized, and accessible manner,
making it easier to collaborate on and maintain your machine learning
projects.
