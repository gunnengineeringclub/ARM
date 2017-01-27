import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.image.BufferedImage;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;


public class Main {

//	public static void main(String[] args) throws IOException {
//		BufferedImage image = ImageIO.read(new File("base.jpg"));
//        for (int x = 0; x < image.getWidth(); x++) {
//            for (int y = 0; y < image.getHeight(); y++) {
//                int c = image.getRGB(x,y);
//                int  red = (c & 0x00ff0000) >> 16;
//                int  green = (c & 0x0000ff00) >> 8;
//                int  blue = c & 0x000000ff;
//
//                if(red == 0 && green == 0 && blue == 0)
//                {
//                	System.out.println(x + " , " + y);
//                }
//
//
//            }
//        }
//
//	}
	public static void main(String args[]) throws Exception {
	    JFrame f = new JFrame("Draw a Red Line");
	    f.setSize(700, 400);
	    f.setLocation(300, 300);

	    final PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("points.txt")));

	    f.setResizable(false);
	    JPanel p = new JPanel() {
	    	ArrayList<Point> a = new ArrayList<Point>();
	        Point pointStart = null;
	        Point pointEnd   = null;
	        {
	            addMouseListener(new MouseAdapter() {
	                public void mousePressed(MouseEvent e) {
	                    pointStart = e.getPoint();
	                }

	                public void mouseReleased(MouseEvent e) {
	                	a.add(pointStart);
	                	a.add(pointEnd);
	                	out.println((pointStart.x / 50.0) - 7);
	                	out.println((pointStart.y / 50.0)+5);
	                	out.println((pointEnd.x / 50.0) - 7);
	                	out.println((pointEnd.y / 50.0)+5);
	                    pointStart = null;
	                }
	            });
	            addMouseMotionListener(new MouseMotionAdapter() {
	                public void mouseMoved(MouseEvent e) {
	                    pointEnd = e.getPoint();
	                }

	                public void mouseDragged(MouseEvent e) {
	                    pointEnd = e.getPoint();
	                    repaint();
	                }
	            });
	        }
	        public void paint(Graphics g) {
	            super.paint(g);
	            if (pointStart != null) {
	                g.setColor(Color.RED);
	                g.drawLine(pointStart.x, pointStart.y, pointEnd.x, pointEnd.y);

	                for(int i = 0; i < a.size(); i+=2)
	                {
	                	g.drawLine(a.get(i).x,a.get(i).y, a.get(i+1).x, a.get(i+1).y);
	                }
	            }
	        }
	    };
	    f.add(p);
	    f.setVisible(true);

	    f.addWindowListener(new WindowAdapter() {
	    	  public void windowClosing(WindowEvent e) {
	    		  out.close();
	    	    //do something
	    	  }
	    	});
	}

}
