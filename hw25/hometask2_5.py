import subprocess
import  os


def shortestResize(input_dir, img_width, output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    current_dir = os.getcwd()
    subprocess.run(['convert', '{}/{}/*.jpg'.format(current_dir, input_dir), '-resize', str(img_width),
                    '{}/{}/face-04.jpg'.format(current_dir, output_dir)])

shortestResize('Source', 200, 'Output')
