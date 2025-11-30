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
        label = Text(label_text, font_size=22).next_to(pointer, DOWN * 0.2)
        return VGroup(pointer, label)
    

    def construct(self):
        
        lenth = len(random_list)
        gap = lenth
        swapped = True
        


        title = Text("Comb Sort Algorithm", color = WHITE).move_to(3 * UP).scale(1.2)
        self.add(title)

        array = VGroup(*[Square().scale(0.4) for i in range(len(random_list))]).arrange(RIGHT, buff=0.15).move_to(1.5 * UP)
        num_text = VGroup(*[Text(str(num)) for num in random_list]).scale(1).arrange(RIGHT).scale(0.65)
        [num_text[i].move_to(array[i].get_center()) for i in range(len(random_list))]

        self.play(Create(array), Create(num_text))

        gap_text = Text(f"Gap: {gap} // 1.3", font_size=28).to_edge(DOWN)
        self.play(Write(gap_text))

        left_pointer = self.create_pointer(num_text[0].get_center(), "Left")
        right_pointer = self.create_pointer(num_text[gap-1].get_center(), "Right")
        self.play(Create(left_pointer), Create(right_pointer))


        while swapped == True or gap != 1:

            gap = NextGap(gap)
            gap_new_text = Text(f"Gap: {gap} // 1.3", font_size=28).to_edge(DOWN)
            self.play(Transform(gap_text, gap_new_text))
            swapped = False

            for index in range(0, lenth - gap):
                self.play(
                left_pointer.animate.move_to(num_text[index].get_center() + DOWN),
                right_pointer.animate.move_to(num_text[index + gap].get_center() + DOWN),
                Indicate(num_text[index]),
                Indicate(num_text[index + gap]),
                run_time=0.3
                )


                if random_list[index] > random_list[index + gap]:
                    self.play(
                num_text[index].animate.move_to(num_text[index + gap].get_center()),
                num_text[index + gap].animate.move_to(num_text[index].get_center()),
                run_time=0.3
                    )
                    num_text[index], num_text[index + gap] = num_text[index + gap], num_text[index]
                    random_list[index], random_list[index + gap] = random_list[index + gap], random_list[index]

                    swapped = True
        
        for i in range(len(num_text)):
            self.play(Indicate(num_text[i], color=GREEN), run_time=0.3)