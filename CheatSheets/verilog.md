### Verilog
- Verilog is a Hardware Description Language (HDL).
- It is a language used for describing a digital system such as a network switch, a microprocessor, a memory, or a flip-flop.
- We can describe any digital hardware by using HDL at any level.
- It is great and specific language for programming spartlet kit extensively used by Design engineers from AMD ,Qualcomm and other industries.

#### I) Literals
```
<size >'<base><number>
```
All of the following are the same:

```
8'b10101111
8'hAF
{4'hA,4'b1111}
{4'hA,{4{1'b1}}}
```

#### II) Module declaration.

//Rule: Use separate file for each module (Filename should be

```
module_name.v):
module module_name (A, B, C);
input A; // Inputs to the module
input [2:0] B; //Convention: one per line
output C; // Output of the module
...
endmodule
```
#### III) Module instantiation

//In file outer_module.v

```
module outer_module (in1, in2, out);
input in1;
input [2:0] in2;
output out;
module_name md (.A(in1), .B(in2), .C(out));
...
endmodule
```
- Rule: Use port mapping. The port A of module module_name is
connected to wire in1 in module outer_module.
#### IV) wire vs reg
a) Rules for usage within module
 - LHS of “continuous assign” should be a wire
 - LHS of “procedural assign” should be reg.
b) Rules for ports
 - Ports are by default of type wire (you can override this by declaring
it as reg)
 - Input ports cannot be declared as reg (Input ports are always wires)
 - Output ports can be either reg or wire
c) Rules for connecting ports while instantiating
 - When instantiating a module, an output port should be connected to
a wire (cannot be connected to reg)
 - When instantiating a module, an input port can be connected to
either a reg or a wire

#### V) Conditional statements  
The conditional statements are similar to those in C. Verilog supports if, if else, case statements.  
a. if statement: 
```
always @(posedge clk)
begin
    if(rst==1'b1)
        q = 0;
    else
        q = q+1;
end
```
The above example shows that if the expression is true, 0 is assigned to q, else q is incremented by 1.  
b. case statements are used for switching between multiple selections. They are similar to (if (case1) ... else if (case2) ... else ...). 
```
module priority_encoder(sel, out);
    input [0:2] sel;
    output [0:7] out;
    reg [0:7] out;
    always @(select) begin
        out = 0;
        case (select)
            0: out[0] = 1;
            1: out[1] = 1;
            2: out[2] = 1;
            3: out[3] = 1;
            4: out[4] = 1;
            5: out[5] = 1;
            6: out[6] = 1;
            7: out[7] = 1;
        endcase
    end
endmodule

```
The above example is a priority encoder which demonstrates the usage of case statement.  
It is important to note that in case statement if multiple matches exist, only the first is evaluated.  

#### VI) Looping Statements  
Looping statements help in executing a statement repeatedly.
```
forever
    #10 clk = ~clk;
```
This generates a clk signal with period of 20 time units.

```
while(rst==0)
    #5 clk = ~clk;
```
This generates a clk signal with period of 10 time units until rst becomes 1.


#### VII) Sequential logic
 - Rule: To create a flip-flop, instantiate the provided dff.v module.
 - Rule: Do not code sequential logic in any other way.
```
dff d0 (
.q(flop_out),
.d(flop_in),
.rst(reset),
.clk(clock)
);
```
#### VIII) Combinational logic
a) Instantiate the provided logic gates (course webpage)
b) assign statement (Continuous assign)
```
wire result;
assign result = s ? A : B;
//result – must always be wire (refer above)
//s, A, B – can be wire or reg
```
c) Procedural assign ( blocking = or non-blocking <=)
```
reg result;
reg err;
always @(s or A or B)
begin
casex(s)
 1'b1:
 begin
 result = A;
 err = 1'b0;
 end
 1'b0:
 begin
 result = B;
 err = 1'b0;
 end
 default:
 begin
 result = 1'bx;
 err = 1'b1;
 end
endcase
end
//result, err – must always be reg (refer above).
//s, A, B – can be wire or reg
```

#### IX) parameter
- Parameterized module definition (in register.v)
```
module register(out, in, wr_en, clk, rst);
parameter WIDTH = 1;
output [WIDTH-1:0] out;
input [WIDTH-1:0] in;
input wr_en;
input clk;
input rst;
dff_en bits[WIDTH-1:0] (
 .q(out),
 .d(in),
 .en(wr_en),
 .clk(clk),
 .rst(rst)
);//dff_en should instantiate the provided dff.v module
endmodule
```
- Instantiating a parameterized module: with default value of the parameter
register r0 (............);
- Instantiating a parameterized module: override the default value
register #(32) r1 (............);
register #(1) r2 (............);  
#### X) Array instantiation
The dff instantiation in the example above is an array instantiation. It
instantiates many flops with names bits[0], bits[1], ..... bits[n]. Note how
the wire 'out' is split across many different instances. Also, the wire
'wr_en' is connected to multiple ports (one each of each instantiation).

#### XI) define
- Keep defines in a separate file (modname_config.v):
```
define LAST_VALUE 4'b1010
```
```
define WIDTH 4
```
- Include the above file in verilog file (modname.v):
```
`include "modname_config.v"
module modname(.........);
.......
wire [`WIDTH-1:0] carry;
assign wire = ~carry & `LAST_VALUE;
.......
endmodule
```
#### XII) Allowed keywords
assign, module, endmodule, input, output, wire, define, parameter

#### XIII) Keywords allowed with stipulations
case, casex, reg, always, begin, end
a) case, casex:
 - Have items for all possible combinations. Use default and err should
be asserted in default.
 - All outputs of case statement should be assigned in all case items.
 - All nets used in RHS of all assigns within case statement and all nets
used as the compare value in case statement should be specified in the
sensitivity list.
b) reg:
 - Can only be used to specify outputs of case/casex statement.
c) always, begin, end:
 - Can only be used to introduce case/casex statement.  

#### XIV) Allowed Operators :
*In list below, shift operators should have the second argument as
constant. (x<<4 is allowed whereas x<<y is not allowed)
```
~m Inversion
m & n Bitwise AND
m|n Bitwise OR
m^n Bitwise XOR
m~^n Bitwose XNOR
&m ReductionAND
~&m Reduction NAND
|m Reduction OR
~|m Reduction NOR
^m Reduction NOR
~^m Reduction XNOR
m==n Equality
m!=n Inequailty
m===n Identity
m!==n Not Identical
m << const Shift left by const bits
m >> const Shift right by const bits
condition ? m : n Ternary
{m, n} concatenation
{m {n}} replicate n (m times)
```

#### XV) Delay Models
Delays allow modelling of rise time, fall time and turn-off time.  
```
#(a) // Produces a rise time delay of 'a' time units.
#(a,b) //Produces a rise time delay and fall time delay of 'a' and 'b' time units respectively.  
#(a,b,c) //Produces a rise time,fall time and turn-off time delay of 'a', 'b' and 'c' time units respectively.
```
Each delay can have minimum, typical and maximum delay specifications in the format 
```
#(x:y:z) // Minimum delay of 'x', Typical delay of 'y' and maximum delay of 'z' time units.
```
#### XVI) Testing your design
a) Design file template to be provided for HW2-HW6 and for the project
(in file foo.v);

```
module foo (in, out, clk, rst, err);
...
endmodule
```
b) _hier.v file to be provided for HW2-HW6 and for the project.
(foo_hier.v):
```
module foo_hier ( in, out )
...
clkrst c0( .clk(clk), .rst(rst), .err(err) );
foo f0 ( .out(out), .in(in), .clk(clk),
 .rst(rst), .err(err) );
endmodule
```
c) The testbench _hier_bench.v file to be developed and submitted by the
student (foo_hier_bench.v)
```
module foo_hier_bench;
foo_hier f0 (....);
...
endmodule
```

#### XVII) System Tasks and Functions  
System tasks are mainly tool specific. Consider the below example  
```
$display("This displays the text within quotes"); //display to screen
$monitor($time, "V=%b, clk=%b",V,clk); //monitor the signals V and clk  
```  
Some of the other standard system tasks and fumctions are:  
i. $time, $realtime - current simulation time
ii. $finish - exit the simulator
iii. $stop - stop the simulator
iv. $setup - setup timing check
v. $hold, $width- hold/width timing check
vi. $setuphold - combines hold and setup
vii. $readmemb/$readmemh - read stimulus patterns into memory
viii. $sreadmemb/$sreadmemh - load data into memory
ix. $getpattern - fast processing of stimulus patterns
x. $history - print command history
xi. $save, $restart, $incsave - saving, restarting, incremental saving
xii. $scale - scaling timeunits from another module
xiii. $scope - descend to a particular hierarchy level
xiv. $showscopes - complete list of named blocks, tasks, modules...
xv. $showvars - show variables at scope
xvi. $fdisplay, $fwrite - writing to a file
xvii. $strobe, $fstrobe - write or display simulation data   


#### XVIII) Scripts

a) Verilog rules check script (Not foolproof)
vcheck-all.sh
b) Name convention check script:
name-convention-check
c) Command line verilog simulation script:
wsrun.pl foo_hier_bench *.v
wsrun.pl -wave foo_hier_bench *.v
d) Synthesis script:
synth.pl-cmd=synth -type=other -top=foo -opt=yes -
file=foo.v,foo_submodule1.v,foo_submodule2.v
XV) Submission rules
HW2-HW6 and project submissions require absolute compliance with
guidelines. Here is how you can do almost everything right, but still
score ZERO:
 - By tampering with the provided template for foo.v and/or foo_hier.v
 - By not submitting the provided testbench components foo_hier.v file
and clkrst.v along with the other verilog files.
 - By not submitting the other provided modules like dff.v, not1.v,
nand3.v etc. which are required to compile your design.
 - By submitting a tar file with a directory structure not matching the
guidelines.
(eg, if you have a wrapper directory over hw1_1, hw1_2 and hw1_3)
(eg, if your verilog files are located within subdirectories inside hw1_1)
(eg, if you submit hw1_1, hw2_2, hw3_3 when you are asked to submit
hw1_1, hw1_2 and hw1_3)
 - By submitting .tar.gz or .zip when you are asked to submit .tar
 - By not running vcheck on verilog files or by not checking the results
after running the script.
 - By not turning in .vcheck.out files for each .v file (except the
testbench components and provided module.)
 - By forgetting to click on the 'Submit' button in dropbox after clicking
the 'Upload' button.
