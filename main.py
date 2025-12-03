# Partially adapted from:
# https://github.com/sumit-sah314/youtube_animations_manim/tree/dsa-visualizations
# Original author: Sumit Sah (MIT License)
from manim import *
from random import randint


random_list = [randint(-100, 100) for num in range(randint(12, 14))]
print(random_list)

def NextGap(gap):
    gap = (gap * 10) // 13 # Integer factor 1.3 * 10 = 13
    if gap < 1:
        return 1
    return gap

class CombSortScene(Scene):
    
    def create_pointer(self, position, label_text, color = GREEN):
        
        pointer = Triangle(fill_opacity = 0, color = color)
        pointer.next_to(position, DOWN).scale(0.2)
        label = Text(label_text, font_size = 22).next_to(pointer, DOWN * 0.2)
        return VGroup(pointer, label)
    

    def construct(self):
        
        lenth = len(random_list)
        gap = lenth
        swapped = True
        
        #c = NumbeerPlane().add_coordinates()
        #self.play(Write(c))

        title = Text("Comb Sort Algorithm").move_to(3 * UP).scale(1.3).set_color(WHITE)
        self.add(title)

        # Create squares for each element in the array
        array = VGroup(*[Square().scale(0.4) for i in range(len(random_list))]).arrange(RIGHT, buff=0.15).move_to(1.5 * UP)
        # Create number labels for each value in the array
        num_text = VGroup(*[Text(str(num)) for num in random_list]).scale(1).arrange(RIGHT).scale(0.65)
        [num_text[i].move_to(array[i].get_center()) for i in range(len(random_list))]

        # Animate array creation
        self.play(Create(array), Create(num_text))


        gap_text = Text(f"Gap: {NextGap(gap)}", font_size = 40).to_edge(DOWN)
        self.play(Write(gap_text))

        # Create pointers to track index comparisons
        left_pointer = self.create_pointer(num_text[0].get_center(), "Left")
        right_pointer = self.create_pointer(num_text[gap-1].get_center(), "Right")
        self.play(Create(left_pointer), Create(right_pointer))


        while swapped or gap != 1:

            if gap >= lenth // 1.3:
                run_time = 1
            else:
                run_time = 0.2


            swapped = False

            # Compare elements at a distance of `gap`
            for index in range(0, lenth - gap):
                
                # Move pointers to the current elements                
                self.play(
                left_pointer.animate.move_to(num_text[index].get_center() + DOWN),
                right_pointer.animate.move_to(num_text[index + gap].get_center() + DOWN),
                Indicate(num_text[index]),
                Indicate(num_text[index + gap]),
                run_time = run_time
                )

                # Update pointer labels with current indices
                new_left_label = Text(str(index), font_size=22).next_to(left_pointer[0], DOWN * 0.5)
                new_right_label = Text(str(index + gap), font_size=22).next_to(right_pointer[0], DOWN * 0.5)

                self.play(
                    Transform(left_pointer[1], new_left_label),
                    Transform(right_pointer[1], new_right_label),
                    run_time = run_time
                )

                # If the current pair is out of order, swap 
                if random_list[index] > random_list[index + gap]:
                    # Highlight swap with red
                    self.play(
                        num_text[index].animate.set_color(RED),
                        num_text[index + gap].animate.set_color(RED),
                        run_time = run_time
                    )

                   # Animate swap movement
                    self.play(
                        num_text[index].animate.move_to(num_text[index + gap].get_center()),
                        num_text[index + gap].animate.move_to(num_text[index].get_center()),
                        run_time = run_time
                    )
                    # Update text and value lists after swap
                    num_text[index], num_text[index + gap] = num_text[index + gap], num_text[index]
                    random_list[index], random_list[index + gap] = random_list[index + gap], random_list[index]

                    swapped = True
                
                else:
                    # Highlight that no swap is needed
                    self.play(
                        num_text[index].animate.set_color(GREEN),
                        num_text[index + gap].animate.set_color(GREEN),
                        run_time = run_time
                    )
                # Reset colors back to white for next comparison
                self.play(
                    num_text[index].animate.set_color(WHITE),
                    num_text[index + gap].animate.set_color(WHITE),
                    run_time = run_time
                )
            # Update gap after each pass
            gap = NextGap(gap)
            gap_new_text = Text(f"Gap: {gap}", font_size = 45).to_edge(DOWN * 2.5)
            self.play(Transform(gap_text, gap_new_text), run_time = run_time)
                
        # Indicate all elements are sorted
        for i in range(len(num_text)):
            self.play(Indicate(num_text[i], color=GREEN), run_time = 0.3)
